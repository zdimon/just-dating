
/* author Dimitry Zharikov zdimon77@gmail.com */

import { Injectable } from '@angular/core';
import {
    HttpRequest,
    HttpHandler,
    HttpEvent,
    HttpInterceptor
  } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SessionService } from './../services/session.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
    token: string;


    constructor(
        private sessionService: SessionService
    ) {
    }

    intercept(req: HttpRequest<any>,
              next: HttpHandler): Observable<HttpEvent<any>> {

        const idToken = this.sessionService.getToken();

        if (req.headers.get('Authorization') !== null) {
            return next.handle(req.clone());
        }

        if (idToken) {

            const cloned = req.clone({
                headers: req.headers.set('Authorization',
                    'Token ' + idToken)
            });

            return next.handle(cloned);
        }

        return next.handle(req.clone());
    }
}