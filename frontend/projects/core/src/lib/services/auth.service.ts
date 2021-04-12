import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

import { Router } from '@angular/router';

// Store
import { Store } from '@ngrx/store';
import * as sessionActions from './../../store/actions/session.action';
import { SessionState } from './../../store/states/session.state';
import * as userActions from './../../store/actions/user.action';
import { UserListState } from './../../store/states/user.state';

// Services
import { SessionService } from './session.service';
import { SnackbarService } from './../services/snackbar.service';
import { WsOnlineService } from './ws-online.service';
import {CentService} from './cent.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private api: ApiService,
    private sessionStore: Store<SessionState>,
    private sessionService: SessionService,
    private sb: SnackbarService,
    private router: Router,
    private socketService: WsOnlineService,
    private userStore: Store<UserListState>,
    private centService: CentService,
  ) { }

  public login(data: any) {
    this.api.login(data).subscribe((rez: any) => {
      this.sessionService.setToken(rez.token);
      this.centService.connect();
      this.sessionStore.dispatch(new sessionActions.LogIn(rez));
      this.api.getUserList().subscribe(data => {
        this.userStore.dispatch(new userActions.UpdateUsers(data));
        });
      this.router.navigate(['index']);
    }, (error) => {
      this.sb.showMessage(error.error.detail);
    })
  }

  public logout() {
     this.centService.disconnect();
     this.sessionStore.dispatch(new sessionActions.LogOut());
     this.sessionService.removeToken();
     this.socketService.disconnect();
     this.api.logout();
  }
}
