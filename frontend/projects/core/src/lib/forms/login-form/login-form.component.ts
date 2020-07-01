
/* author Dmitry Zharikov zdimon77@gmail.com */
import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Validators } from '@angular/forms';
import { ApiService } from './../../services/api.service';
import { SnackbarService } from './../../services/snackbar.service';
import { SessionService } from './../../services/session.service';

import { Store } from '@ngrx/store';
import * as sessionActions from '../../../store/actions/session.action';
import { SessionState } from '../../../store/states/session.state';
import { Router } from '@angular/router';

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
    private sessionService: SessionService,
    private sessionStore: Store<SessionState>,
    private router: Router
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
      this.sessionStore.dispatch(new sessionActions.LogIn(rez));
      this.router.navigate(['index']);
    }, (error) => {
      this.sb.showMessage(error.error.detail);
    })
  }

}
