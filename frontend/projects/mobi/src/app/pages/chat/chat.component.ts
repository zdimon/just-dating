import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {

  token: string;

  constructor(private route:ActivatedRoute) { }

  ngOnInit() {
    this.token = this.route.snapshot.params['token'];
  }

}
