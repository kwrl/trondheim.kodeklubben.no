var config = {
	backendURL: "http://localhost:8080"
};

(function() {
    var app = angular.module('kodeklubb', ['ngRoute']);

	app.config(function($routeProvider) {
		$routeProvider
			.when('/', {
				templateUrl : 'pages/frontPage.html',
				controller  : 'ArticleCtrl'
			})

			.when('/register', {
				templateUrl : 'pages/register.html',
				controller  : 'RegisterCtrl'
			});
	});

	app.factory('authService', function($http) {
		return {
			doLogin: function(credentials, success, error) {
				var promise = $http.post([config.backendURL, "api-auth/login/"].join("/"), credentials);
				promise.success(function(data, status, headers, config) {
					if(success)
						success(data);
				});
				promise.error(function(data, status, headers, config) {
					if(error)
						error(data);
				});
			}
		}
	});

	app.controller('RegisterCtrl', function($scope) {
		// dosomething

		$scope.master = {
			username: "",
			email: "",
			password: ""
		};

		$scope.reset = function() {
			$scope.user = angular.copy($scope.master);
			return true;
		};
	});

    app.controller('UserController', function($scope, authService){
        $scope.credentials = {email:"",password:""};
        var ref = this;

        this.login = function(){
			console.log("test");
			console.dir(authService.doLogin($scope.credentials, function(data) {
				console.log("SUCCESS");
				console.dir(data);
			}, function(data) {
				console.log("ERROR");
				console.dir(data);
			}));
        }

		this.logout = function() {
		
		}
    });

    app.directive('loginForm', function(){
        return {
            restrict:'E',
            templateUrl:'templates/login-form.html',
        };
    });


    app.controller('ArticleCtrl',['$http', function($http){
        this.articles   = [];
        var ref         = this;

        this.get_headers = function() {
            $http.get("http://kwrl.co.uk:8000/news/").success(function(data){
            //$http.get("/kodeklubb/json/article_headers.json").success(function(data){
                ref.articles = data; 
            }).error(function(data){
            });
        };

        this.get_full = function(article){
            if(article.body){
                article.hide = !article.hide; 
            } else {
                $http.get("http://kwrl.co.uk:8000/news/"+article.pk).success(function(data){
                //$http.get("/kodeklubb/json/"+article.id+"/article.json").success(function(data){
                    for(var i=0;i<ref.articles.length;i++){
                        if (ref.articles[i].pk==article.pk){
                            ref.articles[i] = data;
                        }
                    }
                });
            }
        };

        this.get_headers();
        }]);

        app.directive('articleList', function() {
            return {
                restrict:'E',
            templateUrl:'templates/article-list.html',
            };
        });

    })();
