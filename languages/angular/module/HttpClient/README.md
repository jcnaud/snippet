# HttpCient 


## Import the service

On **app/app.module.ts** add :

```ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  ...
  imports: [
    // import HttpClientModule after BrowserModule.
    HttpClientModule,
  ],
  ...
})
```

## Configure the service

On **app/config/config.service.ts** add :
```ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class ConfigService {
  constructor(private http: HttpClient) { }
}
```

