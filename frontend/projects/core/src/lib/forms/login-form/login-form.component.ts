/* author Dmitry Zharikov zdimon77@gmail.com */
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';


// Services
import { AuthService } from './../../services/auth.service';

@Component({
  selector: 'core-login-form',
  templateUrl: './login-form.component.html',
  styleUrls: ['./login-form.component.scss']
})
export class LoginFormComponent implements OnInit {

  loginForm = this.fb.group({
    username: ['', Validators.required ],
    password: ['', Validators.required],
  });

  constructor(
    private fb: FormBuilder,
    private authService: AuthService
  ) {

  }

  ngOnInit() {
  }

  get formControls() {
    return this.loginForm.controls;
  }

  onSubmit() {
    this.authService.login(this.loginForm.value);
  }

}
