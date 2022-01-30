
const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('mail');
const phone = document.getElementById('phone');


form.addEventListener('submit', e => {

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}
const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};


const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const phoneValue = phone.value.trim();

    if(usernameValue === '') {
        setError(username, 'Username is required');
    } else {
        setSuccess(username);
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    }
     else {
        setSuccess(email);
    }
    if(phoneValue === '') {
        setError(phone, 'Password is required');
    } else if (phoneValue.length < 10 ) {
        setError(phone, 'phone must be at least 10 character.')
    } else {
        setSuccess(phone);
    }



};
