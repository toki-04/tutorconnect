function create_account(url){


  const first_name = document.getElementById("firstName").value
  const last_name = document.getElementById("lastName").value
  const middle_initial = document.getElementById("middleInitial").value
  const email = document.getElementById("email").value
  const date_of_birth = document.getElementById("dob").value
  const password = document.getElementById("password").value
  const confirm_password = document.getElementById("confirmPassword").value
  const parent_account = document.getElementById("parentAccount")
  const personal_account = document.getElementById("personalAccount")

  const accept_terms = document.getElementById("acceptTerms")

  if (password !== confirm_password){
    alert("Password do not match!")
    return
  }

  if (password.length < 7){
    alert("Password needs to be atleast 8 characters long!")
  }

  if (!accept_terms.checked){
    alert("Please accept the terms and conditions!")
    return
  }
  

  let account_type = ""

  if (parent_account.checked) {
    account_type = parent_account.value
  }else{
    account_type = personal_account.value
  }



  const data = {
    "first_name": first_name,
    "last_name": last_name, 
    "middle_initial": middle_initial,
    "email": email,
    "date_of_birth": date_of_birth,
    "password": password,
    "account_type": account_type,
  }

  fetch(url, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))
}




