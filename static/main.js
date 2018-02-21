(function(){
  'use strict';

  angular.module('TestApp', [])

  .controller('TestappController', ['$scope', '$log',
      function($scope, $log){
        $scope.getResults = function(){
          $log.log('testtest')
        };
      }]);
}());
