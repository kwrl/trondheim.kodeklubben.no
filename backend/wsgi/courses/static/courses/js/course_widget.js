var app = angular.module('coursesApp', 
    ['ngAnimate', 'courseServices', 'registrationServices', 'userServices']
);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.config(function($resourceProvider) {
      $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.controller('CoursesController', function ($scope, $http, Course, Registration, User) {
    $scope.updateModels = function() {
        $scope.courses = Course.query(function() {
            if($scope.courses==undefined || $scope.courses.length==0) { return; }
            $scope.selectedCourse = $scope.courses[0];
        });
        $scope.registrations = Registration.query();
    };

    $scope.updateModels();
    $scope.users = User.query();

    $scope.userStateClass = "alert-danger";
    
    $scope.updateRegistration = function(reg, type) {
        reg.role = type;
        reg.$update($scope.updateModels);
    };

    $scope.registrationRequest = function(type) {
        var reg = $scope.getRegistrationByUserAndCourse(
            $scope.user().pk,
            $scope.selectedCourse.id
        );

        if(reg != undefined) {
            if(type==-1) {
                reg.$delete($scope.updateModels);
                $scope.updateModels();
            } else {
                $scope.updateRegistration(reg, type);
            }
        } else {
            var registration = new Registration();
            registration.role = type;
            registration.user = $scope.user().pk;
            registration.course = $scope.selectedCourse.id;
            registration.$save($scope.updateModels);
        }
    };

    $scope.getRegistrationByUserAndCourse = function(user, course) {
        for(var i = 0; i < $scope.registrations.length; i++) {
            var reg = $scope.registrations[i];
            if(reg.course == course && reg.user == user) {
                return reg;
            }
        }
        return undefined;
    }

    $scope.user = function() {
        if($scope.users[0]==undefined) {
            return {};
        }
        return $scope.users[0];
    }

    $scope.registeredCourse = function(course) {
        for(var i = 0; i < $scope.registrations.length; i++) {
            if($scope.registrations[i].course == course.id) {
                return true;
            }
        }
        return false;
    };

    $scope.isLoggedIn = function() {
        return $scope.users.length>0;
    };
}).directive('courseManagement', function() {
    return { templateUrl: 'static/courses/directives/course-management.html' };
}).directive('registrationList', function() {
    return { templateUrl: 'static/courses/directives/registration-list.html' };
});
