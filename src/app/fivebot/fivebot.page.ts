import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail } from '@ionic/angular/standalone';

@Component({
  selector: 'app-fivebot',
  templateUrl: './fivebot.page.html',
  styleUrls: ['./fivebot.page.scss'],
  standalone: true,
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonItem,  IonLabel,  IonList, IonThumbnail]})
export class FIVEbotPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
