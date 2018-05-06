function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function get_host(){
  var host = window.location.host;
  var a = host.split('.');
  host = 't1000.' + a[a.length-2] + '.' + a[a.length-1];
  return host;
}

function get_token(){
  if(get_host() == 't1000.analyticsvidhya.com'){
    return 'a40ab11680808ec06176c315303f9df0836225ad';
  } else {
    return 'c39f930d68ce296663b2fdfa59294653680d959b'
  }
}

function get_resolution(){
  return window.screen.height+'*'+window.screen.width
}
//$.cookie('av_54ca86af4072e71c45b2f6dec9a1d86c','asdf');
jQuery.ajax({
  type: 'POST',
  url: 'https://'+get_host()+'/visit-data/',
  beforeSend: function(xhr){
    xhr.setRequestHeader('Authorization','Token '+get_token());
  },
  data:{
    'user':getCookie('av_54ca86af4072e71c45b2f6dec9a1d86c'),
    'location':window.location.href,
    'host':window.location.hostname,
    'resolution':get_resolution(),
  },
  success: function(data){
    //console.log('success');
  },
  error: function(e){
    console.log(e);
  }
})
