var coursesController = function ($scope, $http, Course, Registration, User) {
    $scope.updateRegistrations = function() {
        $scope.registrations = Registration.query();
    };

    $scope.updateCourses = function() {
        $scope.courses = Course.query(function() {
        if($scope.courses==undefined || $scope.courses.length==0) { return; }
            $scope.selectedCourse = $scope.courses[0];
        });
    }

    $scope.updateModels = function() {
        $scope.updateCourses();
        $scope.updateRegistrations();
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
};
