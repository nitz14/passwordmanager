(function () {
  'use strict';

  angular.module('passwordmanagerApp')
    .service('ApiService', ['$http', '$q', '$sce', function ($http, $q, $sce) {

      function buildUrl(uri) {
        return '/api/' + uri;
      }

      return {
        loadServices: loadServices,
        getById: getById,
      };

      function loadServices() {
        return $http.get(buildUrl('servises/'))
          .then(function (response) {
            return response.data;
          });
      }

      function getById(id) {
        return $http.get(buildUrl('servises/'), {
            params: {id: id}
        }).then(function (response) {
            return response.data;
        });
      }
    }]);
})();