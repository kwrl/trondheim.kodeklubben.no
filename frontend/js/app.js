(function() {

    var app = angular.module('kodeklubb', []);

    app.controller('UserController', ['$http', function($http){
        this.credentials = {email:"",password:""};
        var ref = this;

        this.login = function(){
            /*
            var copy = {username:ref.credentials.email, password:ref.credentials.password};
            alert(copy.username);
            $http.post("http://kwrl.co.uk:8000/admin/", copy).error(function(res){
               alert(res); 
            }).then(function(res){
                return res.user;
            });
            */
        };
    }]);

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
            //$http.get("http://kwrl.co.uk:8000/news/get_news_headers/").success(function(data){
            $http.get("/kodeklubb/json/article_headers.json").success(function(data){
                ref.articles = data; 
            }).error(function(data){
            });
        };

        this.get_full = function(article){
            if(article.body){
                article.hide = !article.hide; 
            } else {
                $http.get("/kodeklubb/json/"+article.id+"/article.json").success(function(data){
                    for(var i=0;i<ref.articles.length;i++){
                        if (ref.articles[i].id==article.id){
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
