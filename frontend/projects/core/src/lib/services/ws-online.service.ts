
import { Injectable } from '@angular/core';
import { webSocket } from "rxjs/webSocket";
import { ReplaySubject, BehaviorSubject, Observable, Subscription, interval } from 'rxjs';
import { SessionService } from './session.service';

// Store
import { Store } from '@ngrx/store';
import * as userActions from './../../store/actions/user.action';
import { UserListState } from './../../store/states/user.state';
import * as chatMessageActions from './../../store/actions/chat-message.action';
import { ChatMessageState } from './../../store/states/chat-message.state';


@Injectable({
  providedIn: 'root'
})
export class WsOnlineService {
  connection: any;
  conn_timer$: Observable<any>;
  conn_subscription: Subscription;
  desubscription: Subscription;
  ping$ = new ReplaySubject();
  update_user$ = new ReplaySubject();


  constructor(
    private sessionService: SessionService,
    private userStore: Store<UserListState>,
    private chatMessageStore: Store<ChatMessageState>,
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
    this.desubscription =this.connection.subscribe(
      msg => {
        console.log(msg);
        if ( msg.type === 'user_online' ||  msg.type === 'user_offline' ) {
          this.userStore.dispatch(new userActions.UpdateUser(msg.message));
        }
        if ( msg.type === 'chat_message') {
          this.chatMessageStore.dispatch(new chatMessageActions.UpdateChatMessage(msg.message));
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

  disconnect(){
    this.desubscription.unsubscribe();
  }

}
