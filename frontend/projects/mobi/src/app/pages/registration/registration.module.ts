import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import {CoreModule} from '../../../../../core/src/lib/core.module';
import { RegistrationComponent } from './registration.component';
import { RegistrationPageRoutingModule } from './registration-routing.module';

@NgModule({
  declarations: [RegistrationComponent],
  imports: [
    CommonModule,
    RegistrationPageRoutingModule,
    IonicModule,
    CoreModule
  ]
})
export class RegistrationModule { }
