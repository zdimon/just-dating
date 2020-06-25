import { Injectable } from '@angular/core';
import {MatSnackBar} from '@angular/material/snack-bar';

@Injectable({
  providedIn: 'root'
})
export class SnackbarService {

  constructor(private _snackBar: MatSnackBar) { }

  showMessage(message: string) {
    this._snackBar.open(message, 'Error', {
      duration: 2000,
    });
  }
}
