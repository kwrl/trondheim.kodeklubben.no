var app = angular.module('coursesApp', []);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller('CoursesController', function ($scope, $http) {
    $scope.courses = [];
    $scope.userStateClass = "alert-danger";

    $http.get('/courses/open_courses_json')
    .then(function(res) { 
        $scope.courses = res.data;
    });

    $scope.$watch('selectedCourse', function(newValue, oldValue) {
        $scope.userState = "";
        if(newValue==undefined || newValue.pk==undefined) {
            return;
        }
        $scope.updateUserState(newValue.pk); 
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

        $http.post('/courses/register/'+$scope.selectedCourse.pk+'/', data)
        .then(function() {
            $scope.updateUserState($scope.selectedCourse.pk);
        },
        function() {
        });
    }
});
