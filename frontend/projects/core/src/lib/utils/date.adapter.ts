import {NgModule} from '@angular/core';
import {MatDatepickerModule, MatNativeDateModule, NativeDateAdapter, DateAdapter, MAT_DATE_FORMATS} from '@angular/material';

// extend NativeDateAdapter's format method to specify the date format.
export class CustomDateAdapter extends NativeDateAdapter {
   format(date: Date, displayFormat: Object): string {
      if (displayFormat === 'input') {
         const day = date.getUTCDate();
         const month = date.getMonth() + 1;
         const year = date.getFullYear();
         // Return the format as per your requirement
         return `${year}-${this._to2digit(month)}-${this._to2digit(day)}`;
      } else {
         return date.toDateString();
      }
   }
   private _to2digit(n: number) {
    return ('00' + n).slice(-2);
   } 

   parse(value: any): any {
    if (value) {
        const timestamp = typeof value === 'number' ? value : Date.parse(value);
        let date_regex = /([0-9]{2}[0-9]{1}\d{1})-([0]{1}[1-9]{1}|[1]{1}[0-2]{1})-([0]{1}[1-9]{1}|[12]{1}\d{1}|[3]{1}[01]{1})/; // Can you own regex or remove it.
        if (date_regex.test(value)) {
            return isNaN(timestamp) ? null : new Date(timestamp);
        } else {
            return new Date(undefined);
        }
    }
    else {
        return;
    }

}

   // If required extend other NativeDateAdapter methods.
}


