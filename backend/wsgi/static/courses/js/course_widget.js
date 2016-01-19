var app = angular.module('coursesApp', 
    ['ngAnimate', 'courseServices', 'registrationServices', 'userServices']
);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller('CoursesController', function ($scope, $http, Course, Registration, User) {
    $scope.courses = Course.query();
    $scope.registrations = Registration.query();
    $scope.users = User.query();

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
    };

    $scope.userStateLabels = {
        '-1': "Ikke registrert",
        '0': "Deltager",
        '1': "Veileder",
        '2': "Reserveveileder"
    };

    $scope.registrationRequest = function(type) {
        data = {} ;
        data['sign_up'] = type;
        course_id = $scope.selectedCourse.id;
        var registration = new Registration();
        registration.role = type;
        registration.user = $scope.user().id;
        registration.$save();
    };

    $scope.user = function() {
        if($scope.users[0]==undefined) {
            return {}
        }
        return $scope.users[0];
    }
}).directive('courseManagement', function() {
    return { templateUrl: 'courses/directives/course-management.html' };
});
