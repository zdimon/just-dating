/* author Dmitry Zharikov zdimon77@gmail.com */
import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';


// Store
import { SessionState } from './../../../core/src/store/states/session.state';
import { Store } from '@ngrx/store';
import { selectIsAuth, selectSessionUser } from './../../../core/src/store/selectors/session.selector';
import { UserState } from './../../../core/src/store/states/user.state';

// Services
import { AuthService } from './../../../core/src/lib/services/auth.service';
import { WsOnlineService } from './../../../core/src/lib/services/ws-online.service';
import { CentService } from './../../../core/src/lib/services/cent.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss']
})
export class AppComponent implements OnInit {

  public sessionUser: UserState;
  public isAuth: boolean;


  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private sessionStore: Store<SessionState>,
    private authService: AuthService,
    private wsOnlineService: WsOnlineService,
    private cent: CentService,
  ) {
    this.initializeApp();
    this.sessionStore.select(selectIsAuth).subscribe(data => {
      this.isAuth = data;
    });
    this.sessionStore.select(selectSessionUser).subscribe(data => {
      this.sessionUser = data;
    });

  }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  ngOnInit() {

  }

  logout(){
    this.authService.logout();
  }
}
