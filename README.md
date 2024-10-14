# Segmentação de Clientes utilizando Machine Learning

## Descrição do Problema

Uma loja de varejo online sediada no Reino Unido, visa compreender melhor as características de compra dos seus clientes. As transações ocorreram entre 01/12/2009 e 09/12/2011. A empresa vende principalmente artigos de presente exclusivos para todas as ocasiões. Muitos clientes da empresa são atacadistas.

Fonte dos Dados: https://archive.ics.uci.edu/dataset/502/online+retail+ii

## Objetivo do Projeto

O objetivo é segmentar os clientes em grupos com comportamentos de compras semelhantes. Com isso a empresa pode construir melhores conexões a fim de fidelizar seus clientes e recuperar clientes perdidos.

## Solução

Vou utilizar o modelo RFM (Recência, Frequência e Valor Monetário) que é uma técnica eficaz para segmentar clientes com base em seu comportamento de compra.

**1. Recência (R)** Refere-se ao tempo desde a última compra do cliente. Clientes que compraram recentemente têm maior probabilidade de comprar novamente.<br>
**2. Frequência (F)** Avalia quantas vezes um cliente comprou em um determinado período. Clientes frequentes são valiosos, pois tendem a ter maior lealdade.<br>
**3. Valor Monetário (M)** Refere-se ao total gasto por cada cliente em um determinado período. Clientes que gastam mais são geralmente mais valiosos para o negócio.

**Entregaveis:** 3 relatórios analíticos contendo: 
1. Clientes agrupados por RFM e seus devidos clusters/grupos.
2. Análise, interpretação e sugestões dos Clusters.
3. Tabela contendo a média dos valores de RFM por cluster.

Abaixo segue algumas imagens do projeto. O projeto completo pode ser acessado clicando [aqui](https://github.com/idfelipemalatesta/customers-segmentation/blob/main/notebooks/customers-clustering.ipynb)

Analisando a distribuição dos clientes por RFM:
<img src="images/hist_rfm.png">

Modelagem KMeans com Elbow Method e Silhouette Score:
<img src="images/inercia_silhoutte.png">

Distribuição dos Clientes por Clusters 3D Plot:
<img src="images/clientes_clusters_3d.png">

Visualização dos Clusters por RFM:
<img src="images/cluster_rfm.png">
