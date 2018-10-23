# Angular


## Installation

### Installation npm
```bash
apt-get install npm
```

### Installation angular
```bash
npm install -g @angular/cli
```

### Installation Yarn
Installer Yarn :
ng set --global packageManager=yarn

## Init new project
```bash
ng new my-project
cd my-project
ng serve
```

##
```
ng test # test
ng e2e  # coverage
ng lint # Police d'écriture
```

## Module

Solution 3: Using Ng-Bootstrap
npm install --save @ng-bootstrap/ng-bootstrap bootstrap@4.0.0-alpha.6 font-awesome

Puis dans .angular-cli.json ajouter
```
    "../node_modules/bootstrap/dist/css/bootstrap.min.css",
    "../node_modules/font-awesome/css/font-awesome.min.css"
```

Avec cette solution plus besoin de reseigner les style js (ils sont dans le module alpha)



Add in **app.module.ts**

```python
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
```

Add in root module (app.module.ts)
```
@NgModule({
  declarations: [AppComponent, ...],
  imports: [NgbModule.forRoot(), ...],
  bootstrap: [AppComponent]
})
export class AppModule {
}
```

## Generate a new component
```bash
ng generate component heroes
```


## Generate a new service
```bash
ng generate service hero
```
Create and link to one module
```bash
ng generate service hero --module=app
```

