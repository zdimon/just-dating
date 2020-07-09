
import { Injectable } from '@angular/core';


import {environment} from '../../environments/environment';
import * as Centrifuge from 'centrifuge';
import { SessionService } from './session.service';

// Store
import { Store } from '@ngrx/store';
import * as chatMessageActions from './../../store/actions/chat-message.action';
import { ChatMessageState } from './../../store/states/chat-message.state';


@Injectable({
  providedIn: 'root'
})
export class CentService {

  centrifuge: any;
  token: string;


  constructor(
    private sessionService: SessionService,
    private chatMessageStore: Store<ChatMessageState>
    ) {
    // this.set_reconnector();
    this.connect();
  }



  connect() {
    this.token = this.sessionService.getToken();
    if (this.token) {

      this.centrifuge = new Centrifuge(environment.centUrl);
      this.centrifuge.setToken(environment.centToken);
      this.centrifuge.connect();
      this.dispatcher();
      this.centrifuge.on('disconnect', (context) => {
          console.log('Disconnect....');
      });
      this.centrifuge.on('connect', (context) => {
        console.log('Connection succesfull.');
      });
    }

  }

  dispatcher(){
    this.centrifuge.subscribe(this.token, (message) => {
      console.log(message);
      if ( message.data.type === 'chat_message') {
        this.chatMessageStore.dispatch(new chatMessageActions.UpdateChatMessage(message.data.message));
      }
    });
    this.centrifuge.subscribe('news', (message) => {
      console.log(message);
    });
  }
}
