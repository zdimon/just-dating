import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

import { Router } from '@angular/router';

// Store
import { Store } from '@ngrx/store';
import * as sessionActions from './../../store/actions/session.action';
import { SessionState } from './../../store/states/session.state';

// Services
import { SessionService } from './session.service';
import { SnackbarService } from './../services/snackbar.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private api: ApiService,
    private sessionStore: Store<SessionState>,
    private sessionService: SessionService,
    private sb: SnackbarService,
    private router: Router
  ) { }

  public login(data: any) {
    this.api.login(data).subscribe((rez: any) => {
      this.sessionService.setToken(rez.token);
      this.sessionStore.dispatch(new sessionActions.LogIn(rez));
      this.router.navigate(['index']);
    }, (error) => {
      this.sb.showMessage(error.error.detail);
    })
  }

  public logout() {
     this.sessionStore.dispatch(new sessionActions.LogOut());
     this.sessionService.removeToken();
  }
}
