
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { QuizComponent } from './quiz.component';
import { QuizPageRoutingModule } from './routing';

import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';


@NgModule({
  declarations: [QuizComponent],
  imports: [
    CommonModule,
    QuizPageRoutingModule,
    IonicModule,
    FormsModule
  ]
})
export class QuizModule { }
