#include <stdlib.h>
#include <stdio.h>



#include<stdio.h>
#include<stdlib.h>


typedef struct node{
	int num;
	int data;
	node *next;
}node;

//建立链表，两个指针，p新建节点，q链接前后节点
node *create(int n){
	node *head,*q,*p;
	for(int i=0;i<n;i++){
		p = (node*)malloc(sizeof(node));
		printf("Please input node%d : ", i+1);
		scanf("%d,%d",&p->num,&p->data);
		if(i==0){
			q =p;
			head = p;
			}
			else{
				q->next = p;
				p->next = NULL;
				q = p;
			}
		}
	return head;
}

//释放链表， 两个指针，q删除释放当前节点，p指向下一个
void  drop(node *head){
	node *p,*q;
	if(head = NULL){printf("No link");exit(0);}
	p = q =head;
	while(p!=NULL){
		p=p->next;
		free(q);
		q=p;
	}
	
	if(p == NULL and q == NULL) printf("drop ok \n") ;
	else printf("wrong");
	
}	
		
//展示链表，一个指针
void show(node *head){

	node *p;
	p = head;
	while(p!=NULL){
		printf("num : %d ,data : %d  --> ", p->num,p->data);
		p = p->next;
	}
	printf(" end \n");
	p = NULL;
}

//插入链表,两个指针，q指向插入节点的前一个节点(如果是第一个需要特殊处理)
node* insert(node *head,int n){
	node *p,*q;
	q = head;
	if(n==0) {
		p = (node*)malloc(sizeof(node));
		printf("Please input data after node%d: ", n);
		scanf("%d,%d",&p->num,&p->data);
		p->next = head;
		head = p;
		
		}else{
				int i;
				for(i=0;i<n-1;i++){
					q = q->next;
					}
				p = (node*)malloc(sizeof(node));
				printf("Please input data after node%d: ", n);
				scanf("%d,%d",&p->num,&p->data);
				p->next = q->next;
				q->next = p;
		}
	p = q =NULL;
	return head;
}

//删除节点 , 分首节点和非首节点两种情况
node* del(node *head,int n){
	node *p,*q;
	q = head;
	if(n==1){
		p = head->next;
		free(q);
		head = head->next;
	}
		else{
			for(int i = 1;i< n-1;i++){q = q->next;}
			p = q->next;
			q->next = q->next->next;
			free(p);
		}
		
	p = q = NULL;
	return head;
	}		
	
	
int main(){
	printf("Please input the len of linknode: ");
	int n;
	scanf("%d", &n);
	node *head = create(n);
	show(head);
	
	int m;
	printf("where to insert : ");
	scanf("%d",&m);
	
	head = insert(head,m);
	show(head);
	
	int k;
	printf("where to del : ");
	scanf("%d",&k);
	
	head = del(head,k);
	show(head);
	
	drop(head);	
	scanf("%d", &n);
	return 0;	
	
	
}
