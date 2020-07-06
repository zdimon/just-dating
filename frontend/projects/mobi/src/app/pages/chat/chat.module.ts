import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatComponent } from './chat.component';

import { IonicModule } from '@ionic/angular';
import {CoreModule} from '../../../../../core/src/lib/core.module';
import { ChatPageRoutingModule } from './routing';

@NgModule({
  declarations: [ChatComponent],
  imports: [
    CommonModule,
    IonicModule,
    CoreModule,
    ChatPageRoutingModule,
    FormsModule
  ]
})
export class ChatModule { }
