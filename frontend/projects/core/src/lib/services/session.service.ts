import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SessionService {
  storage: any;

  constructor() { 
    this.storage = sessionStorage;
  }

  getToken(): string {
      return this.storage.getItem('access_token');
  }

  setToken(value: string) {
      this.storage.setItem('access_token', value);
  }

  removeToken() {
      this.storage.removeItem('access_token');
  }
  
}
