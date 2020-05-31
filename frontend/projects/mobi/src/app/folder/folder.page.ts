import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import {ApiService} from '../../../../core/src/lib/services/api.service';

@Component({
  selector: 'app-folder',
  templateUrl: './folder.page.html',
  styleUrls: ['./folder.page.scss'],
})
export class FolderPage implements OnInit {
  public folder: string;
  users = [];

  constructor(
    private activatedRoute: ActivatedRoute,
    private apiService: ApiService) {
      this.apiService.getUserList().subscribe((data: any) => {
        this.users = data; 
      });
     }

  ngOnInit() {
    this.folder = this.activatedRoute.snapshot.paramMap.get('id');
  }

}
