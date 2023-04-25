chrome.tabs.query({currentWindow: true, active: true}, function(tabs) {
    var tab = tabs[0];
    var url = tab.url;
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://localhost:5000?url=' + encodeURIComponent(url));
    xhr.onload = function() {
      document.getElementById('content').innerHTML = xhr.responseText;
    };
    xhr.send();
  });
  