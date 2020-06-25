
/* author Dmitry Zharikov zdimon77@gmail.com */
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { ApiService } from './../../services/api.service';
import { SnackbarService } from './../../services/snackbar.service';
import { SessionService } from './../../services/session.service';

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
    private api: ApiService,
    private sb: SnackbarService,
    private sessionService: SessionService
  ) {

  }

  ngOnInit() {
  }

  get formControls() {
    return this.loginForm.controls;
  }

  onSubmit() {
    this.api.login(this.loginForm.value).subscribe((rez: any) => {
      console.log(rez);
      this.sessionService.setToken(rez.token);
    }, (error) => {
      this.sb.showMessage(error.error.detail);
    })
  }

}
