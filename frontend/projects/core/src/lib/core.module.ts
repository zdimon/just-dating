

import { NgModule } from '@angular/core';
import { CoreComponent } from './core.component'; 
import { HttpClientModule } from '@angular/common/http';
import {ApiService} from './services/api.service';
import { RegistrationFormComponent } from './forms/registration-form/registration-form.component';

import { FormsModule }   from '@angular/forms';

/* Material */
import {MatInputModule} from '@angular/material';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker';

import {MatNativeDateModule} from '@angular/material';
import { MatMomentDateModule } from '@angular/material-moment-adapter';


import { FlexLayoutModule } from '@angular/flex-layout';




@NgModule({
  declarations: [CoreComponent, RegistrationFormComponent],
  imports: [
    HttpClientModule,
    FormsModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    FlexLayoutModule,
    MatButtonModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,

  ],
  exports: [CoreComponent, RegistrationFormComponent, MatNativeDateModule],
  providers: [ApiService
    
  ]
})
export class CoreModule { }
