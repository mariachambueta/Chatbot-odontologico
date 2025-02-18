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
  //Tarjetas de presentación de cada uno
  tarjetas = [
    {
      titulo: "Nicolas Garcia",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Usa sensores para saber cuándo regar.",
      imagen: "/assets/NickP.png"
    },
    {
      titulo: "Valentina Vargas",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Aprende técnicas de hidroponía y macetas.",
      imagen: "https://static.netwrck.com/static/uploads/ai-Help-Bot-HX-Help-Bot.webp"
    },
    {
      titulo: "Maria Alejandra Chambueta",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy Alejandra Chambueta, estudio Ingeniería en Multimedia en la Universidad Militar Nueva Granada. Me encanta la tecnología, el diseño y todo lo que tenga que ver con la creatividad. También me interesa el emprendimiento digital y siempre estoy buscando formas de aprender cosas nuevas y aplicar mis conocimientos en proyectos interesantes.",
      imagen: "https://static.netwrck.com/static/uploads/ai-Atza-Technology.webp"
    },
    {
      titulo: "Stefany Gelvez Quintana",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Soy Tecnóloga en Electrónica y Comunicaciones, egresada de la Universidad Militar Nueva Granada, con disposición de aprender, aportar  lo mejor de mí, trabajar en equipo, adquirir nuevos conocimientos y habilidades. Soy una persona con características de liderazgo al progreso, proactiva, servicial y dedicada para cumplir con mis respectivos objetivos y metas, con capacidad para desarrollar proyectos en el sector de tecnología. Mi objetivo personal es dar mis primeros pasos en una empresa consolidada en el área de mis estudios académicos, a la cual me permita mostrar y desarrollar al máximo mis capacidades y con la cual crecer profesionalmente. Así mismo, para mi objetivo profesional tengo claro que el éxito laboral y el desarrollo profesional, requieren de compromiso, esfuerzo y lealtad, estoy determinada a asumir ese reto dando así mi mayor esfuerzo, cumpliendo a cabalidad las tareas que se me asignen.",
      imagen: "https://static.netwrck.com/static/uploads/ai-MD-T2-Artificial-Intelligence.webp"
    },
    {
      titulo: "Jeimmy cortes",
      subtitulo: "Estudiante Ingenieria Multimedia",
      descripcion: "Aprende técnicas de hidroponía y macetas.",
      imagen: "https://static.netwrck.com/static/uploads/ai-xerkarsa-Emotional.webp"
    }
  ];
}
