import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatComponent } from './chat.component';

import { IonicModule } from '@ionic/angular';

import { ChatPageRoutingModule } from './routing';

@NgModule({
  declarations: [ChatComponent],
  imports: [
    CommonModule,
    IonicModule,
    ChatPageRoutingModule,
    FormsModule
  ]
})
export class ChatModule { }
