var myIframe = document.querySelector('#myIframe');
var myURL= 'http://0.0.0.0/d-solo/7nUQTYV7z/new-dashboard-copy?orgId=1&from=1630549975401&to=1630571575401&panelId=2'

populateIframe(myIframe, myURL, [['Authorization', 'Bearer ' + 'eyJrIjoiWHlsRVE5SFdxdTg1bHd0Q04xaHZFS1QyUGVsMloyaWciLCJuIjoibXlrZXkiLCJpZCI6MX0=']]);

function populateIframe(iframe, url, headers) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.onreadystatechange = handler;
  xhr.responseType = 'blob';
//   xhr.setRequestHeader('Authorization', 'Bearer ' + 'eyJrIjoiWHlsRVE5SFdxdTg1bHd0Q04xaHZFS1QyUGVsMloyaWciLCJuIjoibXlrZXkiLCJpZCI6MX0=');

  headers.forEach(function(header) {
    xhr.setRequestHeader(header[0], header[1]);
  });
  xhr.send();

  function handler() {
    if (this.readyState === this.DONE) {
      if (this.status === 200) {
        iframe.src = URL.createObjectURL(this.response);
      } else {
        console.error('Request failed', this);
      }
    }
  }
}