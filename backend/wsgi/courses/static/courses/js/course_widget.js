var courseServices = angular.module('courseServices', ['ngResource']);

courseServices.factory('Course', ['$resource',
    function($resource) {
        return $resource('rest/courses/:id', {}, {
            query: {method:'GET', params:{courseId:'courses'}, isArray:true}
        });
    }
]);

var app = angular.module('coursesApp', ['courseServices']);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller('CoursesController', function ($scope, $http, Course) {
    console.log(Course.query());
    $scope.courses = Course.query();
    $scope.userStateClass = "alert-danger";

    $scope.$watch('selectedCourse', function(newValue, oldValue) {
        $scope.userState = "";
        if(newValue==undefined || newValue.id==undefined) {
            return;
        }
        $scope.updateUserState(newValue.id); 
    });

    $scope.updateUserState = function(course_id) {
        $http.get('/courses/register/'+course_id+'/')
        .then(function(res) {
            $scope.userState = parseInt(res.data);
        })
    }

    $scope.userStateLabels = {
        '-1': "Ikke registrert",
        '0': "Deltager",
        '1': "Veileder",
        '2': "Reserveveileder"
    }


    $scope.registrationRequest = function(type) {
        data = {} ;
        data['sign_up'] = type;
        
        course_id = $scope.selectedCourse.id;

        $http.post('/courses/register/'+course_id +'/', data)
        .then(function() {
            newobj = Course.get({id:course_id});
            console.log(newobj);
            Object.assign($scope.selectedCourse, newobj);
            console.log($scope.selectedCourse);
            $scope.updateUserState($scope.selectedCourse.id);
        },
        function() {
        });
    }
});
