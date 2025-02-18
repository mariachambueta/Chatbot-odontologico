import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonImg, IonContent, IonHeader, IonTitle, IonToolbar, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail, IonButton, IonGrid, IonRow, IonCol } from '@ionic/angular/standalone';

import { NdgsComponent } from '../components/ndgs/ndgs.component';
/**/
@Component({
  selector: 'app-fivebot',
  templateUrl: './fivebot.page.html',
  styleUrls: ['./fivebot.page.scss'],
  standalone: true,
  imports: [IonImg, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail, IonButton, IonGrid, IonRow, IonCol]})
export class FIVEbotPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
