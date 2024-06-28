/** LOGIN  */
class LoginForm extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({mode: 'closed'});
        
        const template = document.createElement('template');
        template.innerHTML = `
        <style>
            @import url("css/system.css"); /* Add your CSS file paths */
            .form-container {
                /* Add necessary styles */
            }
            /* Other styles */
        </style>
        <div class="form-container">
            <h2>Login</h2>
            <form method="post" class="auth-form">
                <div class="form-group">
                    <label for="id_username">Username:</label>
                    <input type="text" name="username" required id="id_username">
                </div>
                <div class="form-group">
                    <label for="id_password">Password:</label>
                    <input type="password" name="password" required id="id_password">
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
            <a href="/password_reset">Esqueceu a senha?</a>  
        </div>
        `;
        shadow.appendChild(template.content.cloneNode(true));
    }
}
customElements.define('login-form', LoginForm);

/** SIGNUP  */
class SignupForm extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({mode: 'closed'});
        
        const template = document.createElement('template');
        template.innerHTML = `
        <style>
            @import url("css/system.css"); /* Add your CSS file paths */
            .form-container {
                /* Add necessary styles */
            }
            /* Other styles */
        </style>
        <div class="form-container">
            <h2>Cadastrar</h2>
            <form method="post" class="auth-form">
                <div class="form-group">
                    <label for="id_username">Username:</label>
                    <input type="text" name="username" required id="id_username">
                </div>
                <div class="form-group">
                    <label for="id_password1">Password:</label>
                    <input type="password" name="password1" required id="id_password1">
                </div>
                <div class="form-group">
                    <label for="id_password2">Confirm Password:</label>
                    <input type="password" name="password2" required id="id_password2">
                </div>
                <button type="submit" class="btn btn-primary">Cadastrar</button>
            </form>
        </div>
        `;
        shadow.appendChild(template.content.cloneNode(true));
    }
}
customElements.define('signup-form', SignupForm);

/** PASSWORD RESET  */
class ResetPasswordForm extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({mode: 'closed'});
        
        const template = document.createElement('template');
        template.innerHTML = `
        <style>
            @import url("css/system.css"); /* Add your CSS file paths */
            .form-container {
                /* Add necessary styles */
            }
            /* Other styles */
        </style>
        <div class="form-container">
            <h2>Reset de Senha</h2>
            <form method="post" class="auth-form">
                <div class="form-group">
                    <label for="id_email">Email:</label>
                    <input type="email" name="email" required id="id_email">
                </div>
                <button type="submit">Enviar</button>
            </form>
        </div>
        `;
        shadow.appendChild(template.content.cloneNode(true));
    }
}
customElements.define('reset-password-form', ResetPasswordForm);
