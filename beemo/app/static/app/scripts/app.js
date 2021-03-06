'use strict';

var app = angular.module('beemoApp', [
  'ngRoute',
  'nvd3ChartDirectives'
]);

// Route provider config
app.config(['$routeProvider', function($routeProvider) {

  // Route provider URL path directives
  $routeProvider.
    when('/', {redirectTo: '/cluster'}).
    when('/cluster', {controller:'ClusterController', templateUrl: 'static/views/cluster.html'}).

    // Static redirect for other app components
    otherwise({redirectTo: '/static/'});

}]);
