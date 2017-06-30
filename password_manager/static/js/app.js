(function () {
  'use strict';

  angular
    .module('passwordmanagerApp', [])
    .config(function ($httpProvider) {
      $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    })
})();
