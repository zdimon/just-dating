
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IndexComponent } from './index.component';

import { IndexRoutingModule } from './routing';
import { IonicModule } from '@ionic/angular';
import { CoreModule } from './../../../../../core/src/lib/core.module';

@NgModule({
  declarations: [IndexComponent],
  imports: [
    CommonModule,
    IndexRoutingModule,
    IonicModule,
    CoreModule
  ]
})
export class IndexModule { }
