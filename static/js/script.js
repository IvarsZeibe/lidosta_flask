document.getElementById("login-cancel").addEventListener("click", ()=> {
  document.getElementById("login-window").style.display = "none";
});
document.getElementById("register-cancel").addEventListener("click", ()=> {
  document.getElementById("register-window").style.display = "none";
  document.getElementById("login-window").style.display = "flex";
});
document.getElementById('create-account').addEventListener('click', ()=>{
  document.getElementById("login-window").style.display = "none";
  document.getElementById("register-window").style.display = "flex";
});

let loginButton = document.getElementById("login");
if (loginButton != null){
  loginButton.addEventListener("click", ()=> {
    document.getElementById("login-window").style.display = "flex";
  });
}
let logoutButton = document.getElementById('logout');
if (logoutButton != null){
  logoutButton.addEventListener('click', ()=>{
    var url = "/logout";
    var request = new XMLHttpRequest();
    request.open('POST', url, true);
    request.onload = function() {
      document.location.reload();
    };

    request.onerror = function() {
      // request failed
    };
    request.send();
    event.preventDefault();
  });
}

document.getElementById('login-form').addEventListener("submit", (event)=>{
  var url = "/login";
  var request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.onload = function() {
    if(request.responseText == "Invalid login"){
      document.querySelector('#login-form span').textContent = request.responseText;
    }
    if(request.responseText == "Successful"){
      document.location.reload();
    }
  };

  request.onerror = function() {
    // request failed
  };
  request.send(new FormData(event.target));
  event.target.reset();
  event.preventDefault();
});

document.getElementById('register-form').addEventListener("submit", (event)=>{
  var url = "/register";
  var request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.onload = function() {
    if(request.responseText == "Passwords do not match" || request.responseText == "Email already used"){
      document.querySelector('#register-form span').textContent = request.responseText;
    }
    if(request.responseText == "Successful"){
      document.location.reload();
    }
  };

  request.onerror = function() {
    // request failed
  };
  request.send(new FormData(event.target));
  event.target.reset();
  event.preventDefault();
});
