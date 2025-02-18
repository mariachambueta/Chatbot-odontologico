import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonCol, IonGrid, IonRow, IonButton, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle} from '@ionic/angular/standalone';

@Component({
  selector: 'app-cards',
  templateUrl: './cards.page.html',
  styleUrls: ['./cards.page.scss'],
  standalone: true,
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonCol, IonGrid, IonRow, IonButton, IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle]
})
export class CardsPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  tarjetas = [
    {
      titulo: "1Jardinería Inteligente",
      subtitulo: "Monitorea tus plantas",
      descripcion: "Usa sensores para saber cuándo regar.",
      imagen: "https://ionicframework.com/docs/img/demos/card-media.png"
    },
    {
      titulo: "2Cultivo Urbano",
      subtitulo: "Siembra en casa",
      descripcion: "Aprende técnicas de hidroponía y macetas.",
      imagen: "https://ionicframework.com/docs/img/demos/card-media.png"
    },
    {
      titulo: "3Plantas de interior",
      subtitulo: "Cuidados esenciales",
      descripcion: "Consejos para mantener tus plantas saludables.",
      imagen: "https://ionicframework.com/docs/img/demos/card-media.png"
    },
    {
      titulo: "4Jardinería Inteligente",
      subtitulo: "Monitorea tus plantas",
      descripcion: "Usa sensores para saber cuándo regar.",
      imagen: "https://ionicframework.com/docs/img/demos/card-media.png"
    },
    {
      titulo: "5Cultivo Urbano",
      subtitulo: "Siembra en casa",
      descripcion: "Aprende técnicas de hidroponía y macetas.",
      imagen: "https://ionicframework.com/docs/img/demos/card-media.png"
    }
  ];
}
