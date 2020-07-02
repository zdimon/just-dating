
import { Injectable } from '@angular/core';
import { webSocket } from "rxjs/webSocket";
import { ReplaySubject, BehaviorSubject, Observable, Subscription, interval } from 'rxjs';
import { SessionService } from './session.service';


@Injectable({
  providedIn: 'root'
})
export class WsOnlineService {
  connection: any;
  conn_timer$: Observable<any>;
  conn_subscription: Subscription;
  ping$ = new ReplaySubject();

  constructor(
    private sessionService: SessionService
  ) {
      this.set_reconnector();
   }

   set_reconnector(){
    this.conn_subscription = interval(1000).subscribe(dt => {
      console.log(`Try to connect. Attept ${dt}`);
      this.connect();
    });
   }

   dispacher(){
    this.connection.subscribe(
      msg => {
        if ( msg.type === 'online:ping' ) {
          this.ping$.next(msg);
        }
      },
      err => console.log(err),
      () => console.log('complete')
    );
   }

   connect() {
    const token = this.sessionService.getToken();
    if(token) {
      this.conn_subscription.unsubscribe();
      this.connection  = webSocket({
        url: "ws://localhost:7777/online/",
        openObserver: {
          next: () => {
            this.login();
          },
        },
        closeObserver: {
          next: () => {
            this.set_reconnector();
          },
        },
      });
      this.dispacher();
    }
   }

   login() {
      const token = this.sessionService.getToken();
      const message = {action: 'login', data: {
        token ,
        userAgent: window.navigator.userAgent
      }};
      this.connection.next(message);
      console.log(`WS login as ${token}`);
  }

}
