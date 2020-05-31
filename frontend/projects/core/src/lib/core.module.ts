import { NgModule } from '@angular/core';
import { CoreComponent } from './core.component'; 
import { HttpClientModule } from '@angular/common/http';
import {ApiService} from './services/api.service';

@NgModule({
  declarations: [CoreComponent],
  imports: [
    HttpClientModule
  ],
  exports: [CoreComponent],
  providers: [ApiService]
})
export class CoreModule { }
