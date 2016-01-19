var courseServices = angular.module('courseServices', ['ngResource']);
var registrationServices = angular.module('registrationServices', ['ngResource']);
var userServices = angular.module('userServices', ['ngResource']);

courseServices.factory('Course', ['$resource',
    function($resource) {
        return $resource('rest/courses/:id', {}, {
            query: {method:'GET', params:{courseId:'courses'}, isArray:true}
        });
    }
]);

registrationServices.factory('Registration', ['$resource',
    function($resource) {
        return $resource('rest/registrations/:id/', {}, {
            query: {method:'GET', params:{registrationId:'registrations'}, isArray:true},
            delete: {method:'DELETE', params:{id:'@id'}},
            update: {method:'PUT', params:{id:'@id'}}
        });
    }
]);

userServices.factory('User', ['$resource',
    function($resource) {
        return $resource('rest/users/:id', {}, {
        });
    }
]);
