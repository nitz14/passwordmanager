(function () {
  'use strict';

  angular.module('passwordmanagerApp')
    .controller('ServiceController', ['$scope', 'ApiService',
      function ($scope, ApiService) {
        $scope.ServiceList = null;
        $scope.ServiceDetail = null;

        $scope.loadServices = function () {
          ApiService.loadServices()
            .then(function (response) {
                $scope.ServiceList = response;
                $scope.ServiceDetail = null;
            });
        };

        $scope.getService = function (id) {
          ApiService.getById(id)
            .then(function (response) {
                $scope.ServiceDetail = response;
                $scope.ServiceList = null;
            });
        };

        function init() {
          $scope.loadServices();
        }

        init();
      }
    ]);
})();