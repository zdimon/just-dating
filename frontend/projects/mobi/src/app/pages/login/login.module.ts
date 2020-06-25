import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login.component';
import { IonicModule } from '@ionic/angular';
import { LoginRoutingModule } from './routing';
import { CoreModule } from './../../../../../core/src/lib/core.module';

@NgModule({
  declarations: [
    LoginComponent
  ],
  imports: [
    CommonModule,
    LoginRoutingModule,
    IonicModule,
    CoreModule
  ]
})
export class LoginModule { }
