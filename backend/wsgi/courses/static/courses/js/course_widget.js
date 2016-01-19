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

app
.controller('CoursesController', coursesController)
.directive('courseManagement', courseManagementDirective)
.directive('registrationList', registrationListDirective);
