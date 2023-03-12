function initFirebase() {
    // initialize Firebase
  }
  
  function login() {
    const provider = new firebase.auth.GoogleAuthProvider();
    const auth = firebase.auth();
  
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    auth.signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        const user = userCredential.user;
        console.log(user);
        // redirect to user dashboard
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        console.log(errorMessage);
      });
  }
  
  document.getElementById('login-form').addEventListener('submit', (event) => {
    event.preventDefault();
    login();
  });