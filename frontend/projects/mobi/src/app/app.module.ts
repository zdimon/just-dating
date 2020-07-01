/* author Dmitry Zharikov zdimon77@gmail.com */
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import {CoreModule} from '../../../core/src/lib/core.module';

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

// REDUX store
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { StoreModule } from '@ngrx/store';
import { reducers } from '../../../core/src/store/index';

// init service
import { APP_INITIALIZER } from '@angular/core';
import { InitService } from './../../../core/src/lib/services/init.service';
export function init_app(initService: InitService) {
  return () => initService.init();
}


@NgModule({
  declarations: [AppComponent],
  entryComponents: [],
  imports: [
    BrowserModule,
    IonicModule.forRoot(),
    AppRoutingModule,
    CoreModule,
    BrowserAnimationsModule,
    StoreModule.forRoot(reducers),
    StoreDevtoolsModule.instrument()
  ],
  providers: [
    StatusBar,
    SplashScreen,
    { provide: RouteReuseStrategy, useClass: IonicRouteStrategy },
    {
      provide: APP_INITIALIZER,
      useFactory: init_app,
      deps: [InitService],
      multi: true,
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
