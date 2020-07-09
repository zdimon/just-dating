/* author Dmitry Zharikov zdimon77@gmail.com */
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { CoreComponent } from './core.component'; 
import { HttpClientModule } from '@angular/common/http';


import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';

/* Material */
import {MatInputModule} from '@angular/material';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatSelectModule} from '@angular/material/select';
import {MatDatepickerModule} from '@angular/material/datepicker';
import {MatSnackBarModule} from '@angular/material/snack-bar';

import {MatNativeDateModule} from '@angular/material';
import { MatMomentDateModule } from '@angular/material-moment-adapter';
import { FlexLayoutModule } from '@angular/flex-layout';

// components

import { LoginFormComponent } from './forms/login-form/login-form.component';
import { RegistrationFormComponent } from './forms/registration-form/registration-form.component';
import { AvatarComponent } from './widgets/avatar/avatar.component';

// services
import {ApiService} from './services/api.service';
import { SnackbarService } from './services/snackbar.service';
import { SessionService } from './services/session.service';
import { AuthService } from './services/auth.service';
import { WsOnlineService } from './services/ws-online.service';
import { ChatService } from './services/chat.service';
import { CentService } from './services/cent.service';

// Interceptors
import { HTTP_INTERCEPTORS, HttpClient } from '@angular/common/http';
import { AuthInterceptor } from './interceptors/auth.interceptor';

export const interceptorProviders = [
  { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
];



@NgModule({
  declarations: [CoreComponent, RegistrationFormComponent, LoginFormComponent, AvatarComponent],
  imports: [
    HttpClientModule,
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    FlexLayoutModule,
    MatButtonModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatSnackBarModule
  ],
  exports: [
    CoreComponent,
    RegistrationFormComponent,
    MatNativeDateModule,
    RegistrationFormComponent,
    LoginFormComponent,
    AvatarComponent
  ],
  providers: [
    ApiService,
    SnackbarService,
    SessionService,
    interceptorProviders,
    AuthService,
    WsOnlineService,
    ChatService,
    CentService
  ]
})
export class CoreModule { }
